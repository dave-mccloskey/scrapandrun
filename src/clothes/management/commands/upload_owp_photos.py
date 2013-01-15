from django.core.management.base import BaseCommand, CommandError
from clothes.models import *
from datetime import datetime
from django.core.files import File
import os

class Command(BaseCommand):
  args = '<image1 image2 image3 ...>'
  help = 'Uploads all images specified to OutfitWearingProperties if a photo does not already exist'

  FORMAT = '%B%d,%Ybig.jpg'
  def handle(self, *args, **options):
    if not len(args):
      self.stdout.write(' Specify images to upload in format e.g. January1,2013big.jpg\n')
    for arg in args:
      self.handleImg(os.path.dirname(arg), os.path.basename(arg))

  def handleImg(self, img_path, img_name):
    self.stdout.write('Looking @ %s\n' % img_name)
    dt = datetime.strptime(img_name, self.FORMAT)
    self.stdout.write(' Img is for %s\n' % dt)
    
    owp = OutfitWearingProperties.objects.filter(date__date=dt)

    if len(owp) == 0:
      self.stdout.write(' No OWPs for this date; skipping\n')
      return
    if len(owp) > 1:
      self.stdout.write(' More than 1 OWP for this date; skipping\n')
      return

    self.stdout.write(' Single OWP matched, continuing\n')
    
    owp = owp[0]

    if owp.photo:
      self.stdout.write(' OWP already has a photo, skipping\n')
      return
    
    try:
      self.stdout.write(' Opening file\n')
      f = open(os.path.join(img_path, img_name))
      df = File(f)
    
      self.stdout.write(' Saving file to picasa\n')
      owp.photo.save(img_name, df, save=False)
    
      self.stdout.write(' File saving complete\n')
      self.stdout.write(' Updating database\n')
      
      owp.save()
    except IOError as e:
      self.stdout.write(' Problem opening file: %s\n' % e)
