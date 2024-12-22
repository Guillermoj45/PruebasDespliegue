from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('pruebasPruebas', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE usuarios_partitioned (
                user_ptr_id integer NOT NULL,
                avatar varchar(100),
                fecha_nacimiento date,
                fecha_registro timestamp with time zone NOT NULL,
                fecha_ultimo_login timestamp with time zone NOT NULL,
                activo boolean NOT NULL,
                PRIMARY KEY (user_ptr_id, fecha_registro)
            ) PARTITION BY RANGE (fecha_registro);
            """,
            reverse_sql="DROP TABLE usuarios_partitioned;"
        ),
        migrations.RunSQL(
            """
            CREATE TABLE usuarios_2024 PARTITION OF usuarios_partitioned
            FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
            """,
            reverse_sql="DROP TABLE usuarios_2024;"
        ),
    ]