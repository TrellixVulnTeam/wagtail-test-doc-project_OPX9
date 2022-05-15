# Generated by Django 3.0.10 on 2020-09-24 04:47

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks
import wagtailmarkdown.blocks
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('coderedcms', '0018_auto_20200805_1702'),
        ('website', '0011_auto_20200924_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocPageWithMediaAndReuseSupportAndMenu',
            fields=[
                ('coderedpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coderedcms.CoderedPage')),
                ('repeat_in_subnav', models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.", verbose_name='repeat in sub-navigation')),
                ('repeated_item_text', models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text')),
                ('body', wagtail.core.fields.StreamField([('markdown', wagtail.core.blocks.StreamBlock([('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code'))])), ('reuse', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(label='Custom ID', max_length=255, required=False))])), ('content', wagtail.snippets.blocks.SnippetChooserBlock(website.models.ReusableMarkdownContent))])), ('media', website.models.AgoraMediaBlock(icon='media'))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Doc page with media and reuse , menu support',
            },
            bases=('coderedcms.coderedpage', models.Model),
        ),
        migrations.RemoveField(
            model_name='docpagewithmediaandreusesupport',
            name='repeat_in_subnav',
        ),
        migrations.RemoveField(
            model_name='docpagewithmediaandreusesupport',
            name='repeated_item_text',
        ),
    ]
