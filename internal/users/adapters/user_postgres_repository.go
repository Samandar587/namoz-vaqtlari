package adapters

import (
	"github.com/jackc/pgx"
)

type userRepository struct {
	db *pgx.Conn
}

func NewUserRepository(db *pgx.Conn) *userRepository {
	return &userRepository{db: db}
}

func (u *userRepository) UserExists(userID int) (bool, error) {
	var exists int
	sqlStatement := `
	SELECT count(id)
	FROM users
	where id = $1
	`
	err := u.db.QueryRow(sqlStatement, userID).Scan(&exists)
	if err != nil {
		return false, err
	}

	return exists == 1, nil
}
