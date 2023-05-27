def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    week_days = {1:"Sunday", 2:"Monday",3:"Tuesday", 4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
    if day_of_week not in range(1,8):
        return None
    else: 
        return week_days[day_of_week]
        
print(weekday_name(9))
print(weekday_name(0))
print(weekday_name(4))

