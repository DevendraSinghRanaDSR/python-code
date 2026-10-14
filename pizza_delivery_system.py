print('''🍕 WELCOME TO THE PIZZA DELIVERY SERVICE! 🚀
✨ Your ultimate pizza experience starts here! ✨
• 👨‍🍳 Crafted by Experts: Freshly tossed dough, rich tomato sauce, and premium toppings.
• 🧀 Extra Cheesy: Bubbling, melted mozzarella stretched to perfection in every slice.
• 📦 Hot & Fresh: Straight out of the wood-fired oven and rushing right to your doorstep.
• ⏰ Lightning Fast: Reliable delivery because we know hunger can't wait!
• 💳 Easy Payment: Multiple payment options for your convenience.\n''')

size=input("What size of pizza you want to order? S,M or L:").upper()
pepperoni=input("Do you want pepperoni? Y or N:").upper()
extra_cheese=input("Dou you want extra cheese on your pizza?Y or N:").upper()

bill=0
pizza=" "
pepper=" "
cheese=""

if size=="S":
    bill+=10
    pizza="A Small Size Pizza"
elif size=="M":
    bill+=15
    pizza="A Medium Size Pizza"
elif size=="L":
    bill+=20
    pizza="A Large Size Pizza"
if pepperoni=="Y":
    bill+=5
    pepper="Pepperoni"
    print("🔴 Classic Pepperoni – The timeless crowd-pleaser.")
if extra_cheese=="Y":
    cheese="Extra Cheese"
    print("🧀 Extra Cheese – Because one layer of cheese is never enough!")
    bill+=2

print(f'''your order summary: \t
{pizza} with {pepper} and {cheese}''')
print("🍕 Your pizza is being prepared with love and care! 🍕")
print(f'''
💵 Your total bill is: ${bill}

🔥 Thank you for ordering with us! Your hot pizza is already on its way! 🚀 ''')


