import logging
import os

def logging_config():
   if not os.path.exists('data'):
      os.makedirs('data')
      
   logging.basicConfig(
      filename=os.path.join('data', 'app.log'),
      level=logging.DEBUG,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )