package domain

type UserRepository interface {
	Save(user *User) (int, error)
	FindOneByPhoneNumber(phoneNumber string) (*User, error)
	FindByID(userID int) (*User, error)
	UserExists(userID int) (bool, error)
	UserExistByPhone(phone string) (bool, error)
}
