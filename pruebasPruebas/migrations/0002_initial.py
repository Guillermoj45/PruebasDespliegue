from django.db import migrations, connection

def create_partitioned_table(apps, schema_editor):
    if connection.vendor == 'postgresql':
        schema_editor.execute("""
            CREATE TABLE usuarios_partitioned (
                user_ptr_id integer NOT NULL,
                avatar varchar(100),
                fecha_nacimiento date,
                fecha_registro timestamp with time zone NOT NULL,
                fecha_ultimo_login timestamp with time zone NOT NULL,
                activo boolean NOT NULL,
                PRIMARY KEY (user_ptr_id, fecha_registro)
            ) PARTITION BY RANGE (fecha_registro);
        """)
        schema_editor.execute("""
            CREATE TABLE usuarios_2024 PARTITION OF usuarios_partitioned
            FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
        """)

def drop_partitioned_table(apps, schema_editor):
    if connection.vendor == 'postgresql':
        schema_editor.execute("DROP TABLE IF EXISTS usuarios_2024;")
        schema_editor.execute("DROP TABLE IF EXISTS usuarios_partitioned;")

class Migration(migrations.Migration):

    dependencies = [
        ('pruebasPruebas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_partitioned_table, reverse_code=drop_partitioned_table),
    ]