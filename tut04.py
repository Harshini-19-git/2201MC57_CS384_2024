#ques1

class StudentGrades:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grades):
        name = name.lower()
        if name in self.students:
            print(f"{name} already exists. Updating grades.")
        self.students[name] = grades

    def update_grades(self, name, grades):
        name = name.lower()
        if name in self.students:
            self.students[name].extend(grades)
        else:
            print(f"{name} not found. Adding as new student.")
            self.add_student(name, grades)

    def calculate_average(self):
        averages = {}
        for name, grades in self.students.items():
            averages[name] = sum(grades) / len(grades) if grades else 0
        return averages

    def print_averages(self):
        averages = self.calculate_average()
        for name, avg in averages.items():
            print(f"{name.title()} - Average: {avg:.2f}")

    def sort_students(self):
        averages = self.calculate_average()
        sorted_students = []
        for _ in range(len(averages)):
            max_avg = -1
            max_student = None
            for name, avg in averages.items():
                if avg > max_avg and (name, avg) not in sorted_students:
                    max_avg = avg
                    max_student = name
            sorted_students.append((max_student, max_avg))
        for name, avg in sorted_students:
            print(f"{name.title()} - Average: {avg:.2f}")


# Example Usage
grades = StudentGrades()
grades.add_student("Anmol", [85, 90, 88])
grades.add_student("Naresh", [78, 81, 85])
grades.add_student("Neha", [92, 87, 90])
grades.update_grades("anmol", [95])
grades.print_averages()
print("\nSorted Students by Average Grades:")
grades.sort_students()


#ques2 

from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_dict[sorted_word].append(word)
    return anagram_dict

def calculate_frequencies(anagram_dict):
    freq_dict = {}
    for key, group in anagram_dict.items():
        frequency = defaultdict(int)
        for word in group:
            for char in word:
                frequency[char] += 1
        freq_dict[key] = dict(frequency)
    return freq_dict

def find_highest_frequency_group(freq_dict):
    return max(freq_dict.items(), key=lambda x: sum(x[1].values()))

# Example Usage
words = ["listen", "silent", "enlist", "inlets", "google", "goolge", "cat", "tac", "act"]
anagram_dict = group_anagrams(words)
frequencies = calculate_frequencies(anagram_dict)
highest_freq_group = find_highest_frequency_group(frequencies)

print("Anagram Dictionary:")
for key, group in anagram_dict.items():
    print(f"{key}: {group}")

print("\nFrequencies:")
for key, freq in frequencies.items():
    print(f"{key}: {freq}")

print("\nHighest Frequency Group:")
print(highest_freq_group)
