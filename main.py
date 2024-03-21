from playwright.sync_api import sync_playwright

def test_login(email,password):
    # Launch the browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

    # open the website
        page.goto("https://demo.nopcommerce.com/")
    # click on the login link
        page.click("text=Log in")
    # wait for the login page to load
        page.wait_for_load_state("networkidle")

    # Enter Input valid credentials
        page.fill("#Email", "anuraj@gmail.com")
        page.fill("#Password", "anuraj")
        page.click("//button[normalize-space()='Log in']")


    # wait for the login page to load
        page.wait_for_load_state("networkidle")

        # Check if login is successful
        if page.url == "https://demo.nocommerce.com/":
            print("Login successful!")

        else: 
            print("Login failed, invalid credentials")
        # search the item Macbook
        page.fill("#small-searchterms","Macbook")
        page.press("#small-searchterms", "Enter")
        search_results=page.query_selector_all(".product-item")
        if search_results:
          print("Search results found")
        else:
            print("No search results found")

        #click on the Macbook displayed   
        page.click("//h2[@class='product-title']//a[contains(text(),'Apple MacBook Pro 13-inch')]")
        #wait the page to load
        page.wait_for_load_state("networkidle")
        #add the product to cart
        page.click(".button-2.product-box-add-to-cart-button")    
        # wait the page to load
        page.wait_for_load_state("networkidle")
        # check if the item is added to cart
        if search_results:
            print("Added item")
        else:
            print("Not added item")

        page.click("//span[@class='cart-label']")

        if search_results:
            print("Landed cart page")
        else:
            print("Not landed cart page")
        #click on the check out button
        page.click("//button[@id='checkout']")

        # click on the logout icon
        page.click("text=Log out")

        page.wait_for_load_state("networkidle")

        # check if log out is successful
        if page.url =="https://demo.nopcommerce.com/":
            print("Logout successful")
        else:
            print("Logout failed")

        #close the browser
        browser.close()
        
if __name__ == "__main__":
    test_login("anuraj@gmail.com","anuraj")

