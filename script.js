
let orders = JSON.parse(localStorage.getItem("orders") || "[]");

function addItem(name, price) {
    orders.push({ name: name, price: price });

    localStorage.setItem("orders", JSON.stringify(orders));

    alert(name + " added to cart!");
}


function showCart() {
    const cartItems = document.getElementById("cartItems");
    const cartTotal = document.getElementById("cartTotal");

    cartItems.innerHTML = "";
    let total = 0;

    orders.forEach((item, index) => {
        const row = document.createElement("div");
        row.className = "cart-item";

        const name = document.createElement("span");
        name.textContent = item.name;

        const price = document.createElement("span");
        price.textContent = "$" + Number(item.price).toFixed(2);

        // Remove button
        const removeButton = document.createElement("button");
        removeButton.textContent = "Remove";
        removeButton.onclick = function () {
            removeItem(index);
        };

        row.appendChild(name);
        row.appendChild(price);
        row.appendChild(removeButton);

        cartItems.appendChild(row);

        total += Number(item.price);
    });

    cartTotal.textContent = total.toFixed(2);

    document.getElementById("cartWindow").style.display = "block";
}


function removeItem(index) {
    // Remove the selected item
    orders.splice(index, 1);

    // Save the updated cart
    localStorage.setItem("orders", JSON.stringify(orders));

    // Refresh the cart window and total
    showCart();
}


function closeCart() {
    document.getElementById("cartWindow").style.display = "none";
}
function sendOrder() {
    if (orders.length === 0) {
        alert("Your cart is empty!");
        return;
    }

    const pickupTime = document.getElementById("pickupTime").value;

    if (!pickupTime) {
        alert("Please select a pickup time!");
        return;
    }

    alert("Your order was sent! Pickup time: " + pickupTime);

    orders = [];
    localStorage.setItem("orders", JSON.stringify(orders));

    document.getElementById("pickupTime").value = "";
    showCart();
}
