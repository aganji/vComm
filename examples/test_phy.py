# Adding vlc phy to system path
import sys
sys.path.append('..')

# import vlc phy
import tx_phy

# Send test data
tx_phy.send_data('1101001')