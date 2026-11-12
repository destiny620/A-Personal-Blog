from django.db import migrations

import ckeditor_uploader.fields


def replace_null_content(apps, schema_editor):
    blog_post = apps.get_model("blog", "BlogPost")
    blog_post.objects.using(schema_editor.connection.alias).filter(
        content__isnull=True
    ).update(content="")


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            replace_null_content,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
