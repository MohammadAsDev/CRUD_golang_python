package conn

import (
	"fmt"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type MySqlConn struct {
	_Conn *gorm.DB
	_Err  error
}

func NewMysqlConn(user string, password string, db string) Conn {
	dsn := fmt.Sprintf("%s:%s@tcp(127.0.0.1:3306)/%s?charset=utf8mb4&parseTime=True&loc=Local", user, password, db)
	conn, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	return &MySqlConn{
		_Conn: conn,
		_Err:  err,
	}
}

func (mySqlConn *MySqlConn) Err() error {
	return mySqlConn._Err
}

func (mysqlConn *MySqlConn) GetDb() *gorm.DB {
	return mysqlConn._Conn
}

func (conn *MySqlConn) MigrateTypes(typeVars ...any) error {
	for _, type_var := range typeVars {
		err := conn._Conn.AutoMigrate(type_var)
		if err != nil {
			return err
		}
	}
	return nil
}
