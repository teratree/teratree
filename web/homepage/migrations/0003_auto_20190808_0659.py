# Generated by Django 2.2.3 on 2019-08-08 06:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='aside1',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='aside2',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True),
        ),
    ]
