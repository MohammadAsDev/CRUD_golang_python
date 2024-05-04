package types

import "gorm.io/gorm"

type Product struct {
	gorm.Model
	ProductName        string `json:"product_name"`
	ProductDescription string `json:"product_description"`
}

type AddProductRequest struct {
	ProductName        string `json:"product_name"`
	ProductDescription string `json:"product_description"`
}
