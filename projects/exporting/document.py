import io
from html import escape

from django.http import HttpResponse
from django.utils import timezone
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage, Listing

from users.models import User

from ..models import Attribute
from ..models.utils import create_identifier

IMAGE_WIDTH = Mm(136)


def _get_single_display_value(attribute, value):
    if value is None or attribute.value_type == Attribute.TYPE_GEOMETRY:
        return None
    if attribute.value_type == Attribute.TYPE_BOOLEAN:
        return 'Kyllä' if value else 'Ei'  # TODO
    elif attribute.value_type == Attribute.TYPE_DATE:
        return value.strftime('%d.%m.%Y')
    elif attribute.value_type == Attribute.TYPE_USER and isinstance(value, User):
        return value.get_full_name()
    else:
        return escape(str(value))


def get_attribute_display(attribute, value):
    if isinstance(value, list):
        return [_get_single_display_value(attribute, v) for v in value]
    else:
        return _get_single_display_value(attribute, value)


def render_template(project, document_template):
    doc = DocxTemplate(document_template.file)

    attribute_data_display = {}
    attributes = {a.identifier: a for a in Attribute.objects.all()}

    for identifier, value in project.get_attribute_data().items():
        attribute = attributes.get(identifier)

        if not attribute:
            continue

        if attribute.value_type == Attribute.TYPE_IMAGE and value:
            display_value = InlineImage(doc, value, width=IMAGE_WIDTH)
        else:
            display_value = get_attribute_display(attribute, value)

        if display_value is None or display_value == '':
            display_value = escape(' < {} >'.format(attribute.name))
        elif attribute.value_type == Attribute.TYPE_LONG_STRING:
            display_value = Listing(display_value)

        attribute_data_display[identifier] = display_value

    doc.render(attribute_data_display)
    output = io.BytesIO()
    doc.save(output)
    return output.getvalue()


def get_document_response(project, document_template, filename=None):
    if filename is None:
        filename = '{}-{}-{}'.format(create_identifier(project.name), document_template.name, timezone.now().date())

    output = render_template(project, document_template)
    response = HttpResponse(
        output, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename={}.docx'.format(filename)
    return response
