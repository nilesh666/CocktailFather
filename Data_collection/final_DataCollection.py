from data import drinks
from Collection_Class import Collect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# trial = drinks.iloc[:5]
# names = trial['name'].tolist()

names = drinks[90:92]['name'].tolist()
# print(names)

collector = Collect("https://www.thecocktaildb.com")
ingredients = [collector.get_ingredients(i.link) for i in drinks[90:92].itertuples()]
instructions = [collector.get_instructions(i.link) for i in drinks[90:92].itertuples()]

print(ingredients)
print(instructions)
print(names)

form = "https://forms.gle/pAoa2d1B2xpyuarV6"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

d = webdriver.Chrome(options=chrome_options)

for i in range(len(names)):
    d.get(form)
    # top = d.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # middle = d.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # bottom = d.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # submit = d.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    top = WebDriverWait(d, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    middle = WebDriverWait(d, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    bottom = WebDriverWait(d, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    submit = WebDriverWait(d, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'))
    )

    top.send_keys(names[i])
    middle.send_keys(instructions[i])
    bottom.send_keys(ingredients[i])
    submit.click()
#print(names)



