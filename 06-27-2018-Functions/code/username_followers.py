def profile_info(username, followers):
    print('Username: {}'.format(username))
    print('Followers:  {}'.format(followers))


# Call function with parameters assigned as above
profile_info('JessGarson', 452)


# Call function with keyword arguments
profile_info(username='JessGarson',   followers=452)
