# from argparse import ArgumentParser
# parser = ArgumentParser(description="Provide the dealer ids with list format with --today_dealer_ids argument")
# parser.add_argument("--today_dealer_ids", help="list contains dealer ids", type=list)



# dealer_ids_argument = parser.parse_args().today_dealer_ids
# today_dealer_ids = [dealerid for dealerid in dealer_ids_argument.split(',')]

import ast
import sys

# userProvidedDealerList = ast.literal_eval(sys.argv[1])
# userProvidedDealerList = [str(dealerid) for dealerid in userProvidedDealerList]
# print(userProvidedDealerList)


userProvidedDealerList = ast.literal_eval(sys.argv[1])

userProvidedDealerList = [str(dealerid) for dealerid in userProvidedDealerList]
print(userProvidedDealerList)
