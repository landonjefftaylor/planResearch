import datetime as dt
import ics

month_names = [
  "NULL",
  "JAN",
  "FEB",
  "MAR",
  "APR",
  "MAY",
  "JUN",
  "JUL",
  "AUG",
  "SEP",
  "OCT",
  "NOV",
  "DEC"
]

# PAPER STAGES
# Draft
# Draft review
# Proofread
# Coauthor review
# Final review
# Submission

# ARTIFACT STAGES
# Set up artifact
# Document artifact
# Test Artifact in-house
# Third-party artifact test
# Final review
# Submission

def days_before(date, amt):
  td = dt.timedelta(days=amt)
  return date - td

def datestr(date):
  if date.day < 10:
    s_day = str(0) + str(date.day)
  else:
    s_day = str(date.day)
  s_month = str(month_names[date.month])
  s_year = str(date.year)
  return s_day + " " + s_month + " " + s_year

if __name__ == "__main__":

  print("Welcome to the research schedule generator.")

  print("What is the title of your work?")
  title = str(input(":: "))

  confirm = "n"
  while "y" not in confirm.lower():
    year = int(input("What year is " + title + " due? (YYYY) "))
    month = int(input("What month is " + title + " due? (MM) "))
    day = int(input("What day is " + title + " due? (DD) "))
    due_date = dt.date(year,month,day)
    confirm = input("So the paper is due on " + datestr(due_date) + "? (y/n) ")

  artifact = "y" in input("Does this paper require an artifact? (y/n) ").lower()
  if artifact:
    confirm = "n"
    while "y" not in confirm.lower():
      a_year = int(input("What year is the artifact due? (YYYY) "))
      a_month = int(input("What month is the artifact due? (MM) "))
      a_day = int(input("What day is the artifact due? (DD) "))
      a_due_date = dt.date(a_year,a_month,a_day)
      confirm = input("So the artifact is due on " + datestr(a_due_date) + "? (y/n) ")
  
  standard = "y" in input("Do you wish to follow the recommended schedule? (y/n) ").lower()
  if standard: 
    # Spend 3 weeks compiling a draft
    draft_days = 21
    # Spend 2 weeks evaluating the results of the draft
    draft_review_days = 14
    # Spend a week proofreading
    proofread_days = 7
    # Have all authors review for 7 days before submitting
    coauthor_days = 7
    # Do a final review of the paper before submitting
    final_review_days = 4
    # Submit 3 days before deadline to avoid issues
    submission_days = 3
   
    if artifact:
      # Spend a week getting files ready to go
      produce_artifact_days = 7
      # Spend 3 days documenting the artifact
      documentation_days = 3
      # Spend 3 days testing the artifact in-house
      test_inhouse_days = 3
      # Give third parties a week to test the artifact
      test_3party_days = 7
      # Spend 2 days doing a final artifact review
      artifact_review_days = 2
      # Submit 2 days early to avoid issues
      artifact_submission_days = 2
  
  else:
    draft_days = int(input("How many days will you take to write a draft? (default: 21) "))
    draft_review_days = int(input("How many days will you spend evaluating the contents of your draft? (14) "))
    proofread_days = int(input("How many days will you spend proofreading your draft? (7) "))
    coauthor_days = int(input("How many days will you give coauthors to review? (7) "))
    final_review_days = int(input("How many days will you spend on a final review? (4) "))
    submission_days = int(input("How many days early will you submit the paper? (3) "))

    if artifact:
      produce_artifact_days = int(input("How many days will you spend preparing the artifact? (7) "))
      documentation_days = int(input("How many days will you spend producing artifact documentation? (3) "))
      test_inhouse_days = int(input("How many days will you spend on in-house artifact testing? (3) "))
      test_3party_days = int(input("How many days will you give a third party to test your artifact? (7) "))
      artifact_review_days = int(input("How many days will you spend finalizing your artifact? (2) "))
      artifact_submission_days = int(input("How many days early will you submit your artifact? (2) "))

  # WITH DEADLINES RIGHT ON TRACK (PLAN S TANDARD)
  submission_deadline_s = days_before(due_date, submission_days)
  final_review_deadline_s = days_before(submission_deadline_s, final_review_days)
  coauthor_deadline_s = days_before(final_review_deadline_s, coauthor_days)
  proofread_deadline_s = days_before(coauthor_deadline_s, proofread_days)
  draft_review_deadline_s = days_before(proofread_deadline_s, draft_review_days)
  draft_deadline_s = days_before(draft_review_deadline_s, draft_days)
  
  if artifact:
    artifact_submission_deadline_s = days_before(a_due_date, artifact_submission_days)
    artifact_review_deadline_s = days_before(artifact_submission_deadline_s, artifact_review_days)
    test_3party_deadline_s = days_before(artifact_review_deadline_s, test_3party_days)
    test_inhouse_deadline_s = days_before(test_3party_deadline_s, test_inhouse_days)
    documentation_deadline_s = days_before(test_inhouse_deadline_s, documentation_days)
    produce_artifact_deadline_s = days_before(documentation_deadline_s, produce_artifact_days)

  # WITH DEADLINES TIGHTENED BY 1 DAY (PLAN T IGHT)
  submission_deadline_t = days_before(due_date, submission_days-1)
  final_review_deadline_t = days_before(submission_deadline_t, final_review_days-1)
  coauthor_deadline_t = days_before(final_review_deadline_t, coauthor_days-1)
  proofread_deadline_t = days_before(coauthor_deadline_t, proofread_days-1)
  draft_review_deadline_t = days_before(proofread_deadline_t, draft_review_days-1)
  draft_deadline_t = days_before(draft_review_deadline_t, draft_days-1)
  
  if artifact:
    artifact_submission_deadline_t = days_before(a_due_date, artifact_submission_days-1)
    artifact_review_deadline_t = days_before(artifact_submission_deadline_t, artifact_review_days-1)
    test_3party_deadline_t = days_before(artifact_review_deadline_t, test_3party_days-1)
    test_inhouse_deadline_t = days_before(test_3party_deadline_t, test_inhouse_days-1)
    documentation_deadline_t = days_before(test_inhouse_deadline_t, documentation_days-1)
    produce_artifact_deadline_t = days_before(documentation_deadline_t, produce_artifact_days-1)

  # WITH DEADLINES TIGHTENED BY 1 DAY (PLAN L OOSE)
  submission_deadline_l = days_before(due_date, submission_days+2)
  final_review_deadline_l = days_before(submission_deadline_l, final_review_days+2)
  coauthor_deadline_l = days_before(final_review_deadline_l, coauthor_days+2)
  proofread_deadline_l = days_before(coauthor_deadline_l, proofread_days+2)
  draft_review_deadline_l = days_before(proofread_deadline_l, draft_review_days+2)
  draft_deadline_l = days_before(draft_review_deadline_l, draft_days+2)
  
  if artifact:
    artifact_submission_deadline_l = days_before(a_due_date, artifact_submission_days+2)
    artifact_review_deadline_l = days_before(artifact_submission_deadline_l, artifact_review_days+2)
    test_3party_deadline_l = days_before(artifact_review_deadline_l, test_3party_days+2)
    test_inhouse_deadline_l = days_before(test_3party_deadline_l, test_inhouse_days+2)
    documentation_deadline_l = days_before(test_inhouse_deadline_l, documentation_days+2)
    produce_artifact_deadline_l = days_before(documentation_deadline_l, produce_artifact_days+2)


  with open("plan.txt", "w") as f:
    f.write("SCHEDULE FOR " + title.upper() + ":\n")
    f.write("Formal paper due date is " + datestr(due_date))
    if artifact:
      f.write("Artifact due date is " + datestr(a_due_date))

    f.write("\n\n")

    f.write("STANDARD PLAN\n")
    f.write("Finish draft by    " + datestr(draft_deadline_s) + "\n")
    f.write("Review draft by    " + datestr(draft_review_deadline_s) + "\n")
    f.write("Proofread draft by " + datestr(proofread_deadline_s) + "\n")
    f.write("Coauthor review by " + datestr(coauthor_deadline_s) + "\n")
    f.write("Final review by    " + datestr(final_review_deadline_s) + "\n")
    f.write("Submit paper by    " + datestr(submission_deadline_s) + "\n")
    if artifact:
      f.write("---\nMake artifact by   " + datestr(produce_artifact_deadline_s) + "\n")
      f.write("Write art. docs by " + datestr(documentation_deadline_s) + "\n")
      f.write("Test in-house by   " + datestr(test_inhouse_deadline_s) + "\n")
      f.write("3rd party tests by " + datestr(test_3party_deadline_s) + "\n")
      f.write("Final review by    " + datestr(artifact_review_deadline_s) + "\n")
      f.write("Submit artifact by " + datestr(artifact_submission_deadline_s) + "\n")
    f.write("\n")

    f.write("TIGHT PLAN\n")
    f.write("Finish draft by    " + datestr(draft_deadline_t) + "\n")
    f.write("Review draft by    " + datestr(draft_review_deadline_t) + "\n")
    f.write("Proofread draft by " + datestr(proofread_deadline_t) + "\n")
    f.write("Coauthor review by " + datestr(coauthor_deadline_t) + "\n")
    f.write("Final review by    " + datestr(final_review_deadline_t) + "\n")
    f.write("Submit paper by    " + datestr(submission_deadline_t) + "\n")
    if artifact:
      f.write("---\nMake artifact by   " + datestr(produce_artifact_deadline_t) + "\n")
      f.write("Write art. docs by " + datestr(documentation_deadline_t) + "\n")
      f.write("Test in-house by   " + datestr(test_inhouse_deadline_t) + "\n")
      f.write("3rd party tests by " + datestr(test_3party_deadline_t) + "\n")
      f.write("Final review by    " + datestr(artifact_review_deadline_t) + "\n")
      f.write("Submit artifact by " + datestr(artifact_submission_deadline_t) + "\n")
    f.write("\n")

    f.write("LOOSE PLAN\n")
    f.write("Finish draft by    " + datestr(draft_deadline_l) + "\n")
    f.write("Review draft by    " + datestr(draft_review_deadline_l) + "\n")
    f.write("Proofread draft by " + datestr(proofread_deadline_l) + "\n")
    f.write("Coauthor review by " + datestr(coauthor_deadline_l) + "\n")
    f.write("Final review by    " + datestr(final_review_deadline_l) + "\n")
    f.write("Submit paper by    " + datestr(submission_deadline_l) + "\n")
    if artifact:
      f.write("---\nMake artifact by   " + datestr(produce_artifact_deadline_l) + "\n")
      f.write("Write art. docs by " + datestr(documentation_deadline_l) + "\n")
      f.write("Test in-house by   " + datestr(test_inhouse_deadline_l) + "\n")
      f.write("3rd party tests by " + datestr(test_3party_deadline_l) + "\n")
      f.write("Final review by    " + datestr(artifact_review_deadline_l) + "\n")
      f.write("Submit artifact by " + datestr(artifact_submission_deadline_l) + "\n")
    f.write("\n")

  print("Complete. See plan.txt for your plan.")
