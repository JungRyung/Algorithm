##### 한국 조폐공사 #####
def solution(money, costs):
    answer = 0

    coin = [1,5,10,50,100,500]
    cost_rates = []
    for i in range(6):
        cost_rates.append((costs[i]/coin[i],coin[i]))
    
    cost_rates.sort()
    for cost_rate in cost_rates:
        answer += (money // cost_rate[1]) * costs[coin.index(cost_rate[1])]
        money %= cost_rate[1]

    return answer

money = 4873
costs = [1,15,9,35,20,1000]

answer = solution(money, costs)
print(answer)