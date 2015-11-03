def read_prompts(filename):
    infile = open(filename, 'r')
    infile.readline()
    prompt_list = []
    for line in infile:
        if line.strip() != "***end of prompts***":
            prompt_list += [line.strip()]
        else:
            break
    infile.close()
    return prompt_list

def ask_prompts(prompt_list):
    responses = [''] * len(prompt_list)

    for i in range(len(prompt_list)):
        responses[i] = "a"
    return responses

def read_template(filename):
    infile = open(filename, 'r')
    line = ""
    while line.strip() != "***end of prompts***":
        line = infile.readline()

    line = infile.readline()
    template = []
    while line != "":
        template += [line]
        line = infile.readline()
    infile.close()

    return template

def replace_prompts(line, answers):
    start_replace = line.find("[")

    sections = line.split("|")
    index = 1
    while index < len(sections):
        sections[index] = answers[int(sections[index])]
        index += 2
    return "".join(sections)

def word_template(filename):
    prompts = read_prompts(filename)
    answers = ask_prompts(prompts)
    template = read_template(filename)
    print ""
    for line in template:
        print replace_prompts(line, answers),

word_template("Chinchillas.txt")
