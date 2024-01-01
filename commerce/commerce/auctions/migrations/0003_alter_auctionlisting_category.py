# Generated by Django 5.0 on 2023-12-31 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting_bid_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(choices=[('MOT', 'Motors'), ('FAS', 'Fashion'), ('ELE', 'Electronics'), ('ART', 'Collectibles & Art'), ('HGA', 'Home & Garden'), ('SPO', 'Sporting Goods'), ('TOY', 'Toys'), ('BUS', 'Business & Industrial'), ('MUS', 'Music')], default='MOT', max_length=3),
        ),
    ]