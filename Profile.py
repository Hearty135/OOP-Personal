class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
     self.name = name
     self.favorite_language = hobby
     self.hobby = hobby
     self.tech_stack = tech_stack
     self.github_username = github_username
     self.fun_fact = fun_fact

    def introduce(self):
     print(f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")

    def show_stack(self):
     print("My tech stack includes:")
    for tool in self.tech_stack:
        print(f"- {tool}")

    def github_link(self):
     return f"https://github.com/{self.github_username}"

my_profile = Profile(
    name="Mangeni Hearty Martha",
    favorite_language="Python",
    hobby="Writing poems",
    tech_stack=["Python", "HTML"],
    github_username="Hearty135",
    fun_fact="I can compile a poem in a day."
)

my_profile.introduce()
my_profile.show_stack()
print(f"You can find me on GitHub at: {my_profile.github_link()}")