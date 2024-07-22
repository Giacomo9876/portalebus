# Generated by Django 4.2.5 on 2024-07-16 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fornitore",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("idfornitore", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
                ("cognome", models.CharField(max_length=100)),
                ("azienda", models.CharField(max_length=200)),
                ("ente_pubblico", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RichiestaStd",
            fields=[
                ("idrichiestastd", models.AutoField(primary_key=True, serialize=False)),
                ("numero_passeggeri", models.IntegerField()),
                ("numero_giorni", models.IntegerField()),
                ("data_inizio", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="TipoRichiesta",
            fields=[
                (
                    "idtiporichiesta",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("stato_richiesta", models.CharField(max_length=100)),
                ("acronimo", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="TipoServizio",
            fields=[
                ("idtiposervizio", models.AutoField(primary_key=True, serialize=False)),
                ("tipo_servizio", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Utente",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("idutente", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
                ("cognome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("ente_pubblico", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Servizio",
            fields=[
                ("idservizio", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                ("luogo_partenza", models.CharField(max_length=200)),
                ("destinazione", models.CharField(max_length=200)),
                ("km_percorsi", models.FloatField()),
                ("ora_partenza", models.TimeField()),
                ("ora_arrivo", models.TimeField()),
                (
                    "richiesta_std",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="utenza.richiestastd",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="richiestastd",
            name="tipo_richiesta",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="utenza.tiporichiesta"
            ),
        ),
        migrations.AddField(
            model_name="richiestastd",
            name="tipo_servizio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="utenza.tiposervizio"
            ),
        ),
        migrations.AddField(
            model_name="richiestastd",
            name="utente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="utenza.utente"
            ),
        ),
    ]
