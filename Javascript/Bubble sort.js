let list = [];

for (let x = 0; x < list.length; x++) {
    let index = 0;
    while ((index + 1) < list.length) {
        if (list[index] > list[index + 1]) {
            let var1 = list[index];
            let var2 = list[index + 1];
            list[index] = var2
            list[index + 1] = var1
        };
        index = index + 1
    };
};

console.log(list)