senior_project_database= {}
name = input("Please enter your name: ")
major = input("Please enter your major: ")
interest = input("Please enter your technology interest: ")
skill_goal = input("Please enter your skill goal: ")
senior_project_database[name] = {
    "major": major,
    "interest": interest,
    "skill_goal": skill_goal
}
print(f"\n\n\tSenior Project Developer Profile\nName: {name}\nMajor: {major}\nTechnology Interest: {interest}\nSkill Goal: {skill_goal}")

decision = input("\n\nWould you like to add another developer profile? (yes/no): ")
if decision.lower() not in ["yes", "no"]:
    print("Invalid input. Please enter 'yes' or 'no'.")
    decision = input("\n\nWould you like to add another developer profile? (yes/no): ")
while decision.lower() == "yes":
    name = input("Please enter your name: ")
    major = input("Please enter your major: ")
    interest = input("Please enter your technology interest: ")
    skill_goal = input("Please enter your skill goal: ")
    senior_project_database[name] = {
        "major": major,
        "interest": interest,
        "skill_goal": skill_goal
    }
    print(f"\n\n\tSenior Project Developer Profile\nName: {name}\nMajor: {major}\nTechnology Interest: {interest}\nSkill Goal: {skill_goal}")
    decision = input("\n\nWould you like to add another developer profile? (yes/no): ")
print("\n\nThank you for using the Senior Project Developer Profile application! Here are the profiles you entered:")
for name, profile in senior_project_database.items():
    print(f"\nName: {name}")
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")