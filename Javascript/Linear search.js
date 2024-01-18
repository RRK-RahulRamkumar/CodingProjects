let list = [1, 4, 2, 6, 8];

let find_item = Number(prompt("Item to find"));
let found_item = false;

for (let index = 0; index < list.length; index++) {
    if (list[index] === find_item) {
        alert("Found item")
        found_item = true;
        break
    };
};

if (found_item === false) {
    alert("Did not find item")
};
