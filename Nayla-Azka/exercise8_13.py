# Exercise 8-13: User Profile
def buildProfile(first, last, **userInfo):
    """Membangun dictionary yang berisi segala hal tentang pengguna"""
    userInfo['firstname'] = first
    userInfo['lastName'] = last
    return userInfo

userProfile = buildProfile( 
    'nayla',
    'azka',
    lokasi='surakarta',
    hobi='dance',
    jurusan='teknik industri'
)

print(userProfile)