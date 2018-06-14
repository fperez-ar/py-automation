from selene.api import *
import time
#config.start_maximized=True
#hold_browser_open
#counter
#reports_folder
#desired_capabilities

#firefox doesn't work ?
config.browser_name = 'chrome'
browser.open_url('https://www.google.nl/maps')
s('#searchboxinput').set_value('Tokio, Japan').press_enter()
s('h1').should(have.exact_text('Tokio'))
print("Success!")
time.sleep(10)
