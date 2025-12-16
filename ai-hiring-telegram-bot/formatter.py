def format_message(type_, role, company, location, pay, desc):
    tag = ""

    if type_.lower() == "job":
        tag = "#job"
    elif type_.lower() == "internship":
        tag = "#internship"
    elif type_.lower() == "hackathon":
        tag = "#hackathon"

    message = f"""
🚨 Hiring Alert – {type_}

Role: {role}
Company/Organizer: {company}
Location: {location}
Salary/Stipend: {pay}

Short Description:
{desc}

{tag}
"""
    return message.strip()
