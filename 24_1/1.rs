use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("1.txt")?; // Replace "file.txt" with your file path
    let reader = io::BufReader::new(file);

    let mut array1 = Vec::new(); // First array
    let mut array2 = Vec::new(); // Second array

    for line in reader.lines() {
        let line = line?; // Unwrap the Result to get the line
        let numbers: Vec<i32> = line
            .split_whitespace() // Split the line by whitespace
            .filter_map(|num| num.parse::<i32>().ok()) // Parse each part as an i32, ignoring invalid parts
            .collect(); // Collect parsed numbers into a vector

        if numbers.len() == 2 {
            array1.push(numbers[0]); // Add the first number to array1
            array2.push(numbers[1]); // Add the second number to array2
        }
    }

    let mut total_dist = 0;

    // Print the arrays
    // println!("Array 1: {:?}", array1);
    // println!("Array 2: {:?}", array2);
    // process::exit(1);

    array1.sort();
    array2.sort();

    for i in 0..array1.len() {
        total_dist += (array1[i] - array2[i]).abs()
    }

    println!("{}", total_dist);

    let mut frequency = HashMap::new(); // Create an empty HashMap

    for &num in &array2 {
        *frequency.entry(num).or_insert(0) += 1; // Increment count for each element
    }

    let mut total_sim = 0;

    for i in 0..array1.len() {
        if let Some(&freq) = frequency.get(&array1[i]) {
            total_sim += array1[i] * freq; // Multiply array1[i] by its frequency
        }
    }

    println!("{}", total_sim);

    Ok(())
}
