from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import reasearch_task, write_task

# To call this in a sequential manner, form a tech-focused crew with enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[reasearch_task, write_task],
    process=Process.sequential,  # This is optional because sequential is default
    memory=True,  # Remember previous interactions within the same run
    cache=True,  # Reuse previous responses for identical prompts (saves tokens, cost, and time)
    max_rpm=100,
    share_crew=True
)

#start the task execution process with feedback
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL VS Data Science'})
print(result)
