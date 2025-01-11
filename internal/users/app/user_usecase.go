package app

import (
	"golang-project-template/internal/users/domain"
)

type userUsecase struct {
	userRepository domain.UserRepository
}

type UserUsecase interface {
	UserExists(id int) (bool, error)
}

func NewUserUsecase(userRepository domain.UserRepository) UserUsecase {
	return &userUsecase{
		userRepository: userRepository,
	}
}

func (u *userUsecase) UserExists(id int) (bool, error) {
	userExists, err := u.userRepository.UserExists(id)
	if err != nil {
		return false, err
	}

	return userExists, nil

}
