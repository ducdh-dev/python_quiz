def chess_teams(smarties, cleveries):
    return [*zip(smarties, cleveries)]  # * to unzip  # to unzip map use: zip(*map)


smarties = ["Jane", "Bob", "Peter"]
cleveries = ["Oscar", "Lidia", "Ann"]

print(chess_teams(smarties, cleveries))
