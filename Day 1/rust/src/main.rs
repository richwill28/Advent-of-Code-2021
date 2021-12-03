fn read_lines() -> Vec<i32> {
    let file = include_str!("../../input.txt");
    file.lines()
        .map(|line| line.parse::<i32>().unwrap())
        .collect()
}

fn part_one() {
    let mut counter = 0;
    let measurements = read_lines();
    for i in 1..measurements.len() {
        if measurements[i] > measurements[i - 1] {
            counter += 1;
        }
    }
    println!("{}", counter);
}

fn part_two() {
    let mut counter = 0;
    let measurements = read_lines();
    for i in 0..(measurements.len() - 3) {
        let first_window = measurements[i] + measurements[i + 1] + measurements[i + 2];
        let second_window = measurements[i + 1] + measurements[i + 2] + measurements[i + 3];
        if second_window > first_window {
            counter += 1;
        }
    }
    println!("{}", counter);
}

fn main() {
    part_one();
    part_two();
}
