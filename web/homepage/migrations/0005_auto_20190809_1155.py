# Generated by Django 2.2.3 on 2019-08-09 11:55

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_templatepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatepage',
            name='region1',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templatepage',
            name='region2',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templatepage',
            name='region3',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templatepage',
            name='region4',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templatepage',
            name='region5',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templatepage',
            name='region6',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, null=True),
        ),
    ]
