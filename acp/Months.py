import calendar

def display_all_months():
  """Displays the names of all 12 months."""
  for i in range(1, 13):
    month_name = calendar.month_name[i]
    print(month_name)

if __name__ == "__main__":
  display_all_months()