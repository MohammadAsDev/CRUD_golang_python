package conn

import "gorm.io/gorm"

type Conn interface {
	MigrateTypes(typeVars ...any) error
	GetDb() *gorm.DB
	Err() error
}
