birth_year = int(input("Enter your birth year: "))
print(
    f"Birth Year: {birth_year}",
    f"Baby Boomer: {1946 <= birth_year <= 1964}",
    f"Gen X: {1965 <= birth_year <= 1980}",
    f"Millennial: {1981 <= birth_year <= 1996}",
    f"Gen Z: {1997 <= birth_year <= 2012}",
    f"Gen Alpha: {2013 <= birth_year <= 2025}",
    sep='\n'
)