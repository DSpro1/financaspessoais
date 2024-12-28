# Generated by Django 5.1.4 on 2024-12-24 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardFatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('method_payment', models.CharField(choices=[('debit', 'débito'), ('credit', 'crédito')], default='debito', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('valor', models.FloatField()),
                ('profit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('tipo', models.CharField(choices=[('creditor', 'Credor'), ('deptor', 'Devedor')], default='deptor', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('value', models.FloatField()),
                ('status', models.CharField(choices=[('pago', 'pago'), ('a pagar', 'a pagar')], default='recebido', max_length=20)),
                ('modality', models.CharField(choices=[('health', [('gym', 'academia'), ('pharmacy', 'farmácia'), ('exams', 'exames'), ('doctorAppointment', 'consulta')]), ('food', [('market', 'mercado'), ('snackBar', 'lanchone'), ('bakey', 'padaria')]), ('education', [('school', 'escola'), ('publicTender', 'concurso'), ('faculty', 'faculdade')]), ('transport', [('van', 'van'), ('bus', 'onibus')]), ('leisure', [('cinema', 'cinema'), ('park', 'parque'), ('party', 'festa')]), ('loan', [('consignado', 'consignado'), ('informal', 'informal')]), ('donation', [('gift', 'presente'), ('alms', 'esmola')]), ('house', [('reform', 'reforma'), ('forniture', 'móveis'), ('conta_agua', 'conta de água'), ('conta_luz', 'conta de luz')]), ('outhers', [('beautifull', 'beleza'), ('plano_funeraria', 'plano funerária'), ('seguro_vida', 'plano de vida'), ('seguro_carro', 'seguro de carro'), ('credito_celular', 'credito para celular')]), ('vestuario', 'vestuario')], max_length=20)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.cardfatura')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.person')),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('value', models.FloatField()),
                ('status', models.CharField(choices=[('recebido', 'recebido'), ('a receber', 'a receber')], default='recebido', max_length=20)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.cardfatura')),
            ],
        ),
    ]