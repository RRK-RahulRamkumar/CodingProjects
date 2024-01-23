let list = [2, 8, 5, 3, 9, 4];
let main_index = 1;

while (main_index <= (list.length) - 1) {
    let temp_index = main_index;

    while ((temp_index - 1) > -1) {
        if (list[temp_index] < list[temp_index - 1]) {
            let var1 = list[temp_index];
            let var2 = list[temp_index - 1];
            list[temp_index] = var2;
            list[temp_index - 1] = var1;
        };
        temp_index = temp_index - 1;
    };
    main_index = main_index + 1;
};

console.log(list);
