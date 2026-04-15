def calculate_sum(x:int,y:int):
    """
    function to return sum
    """
    return x+y
    
total_sum = 10
bonus_points = 20
final_score=calculate_sum(total_sum,bonus_points)
print(f"Datatype of total sum is {type(total_sum)} and \n"+ f"Datatype of bonus_points is {type(bonus_points)}")
print(f"The final score is {final_score}")