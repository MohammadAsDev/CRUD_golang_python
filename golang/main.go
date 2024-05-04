package main

import (
	"github.com/MohammadAsDev/CRUD_golang_python/conn"
	"github.com/MohammadAsDev/CRUD_golang_python/handlers"
	"github.com/MohammadAsDev/CRUD_golang_python/types"
	"github.com/gin-gonic/gin"
)

func main() {

	mysql_conn := conn.NewMysqlConn("root", "mypass", "test_db")
	if mysql_conn.Err() != nil {
		panic(mysql_conn.Err())
	}

	mysql_conn.MigrateTypes(types.Product{})
	product_handler := handlers.ProductHandler{
		Db: mysql_conn,
	}

	router := gin.Default()
	product_routes := router.Group("/products")

	product_routes.GET("/", product_handler.ListProducts)
	product_routes.POST("/", product_handler.CreateProduct)
	product_routes.PUT("/:id", product_handler.UpdateProduct)
	product_routes.GET("/:id", product_handler.GetProduct)
	product_routes.DELETE("/:id", product_handler.DeleteProduct)

	router.Run("127.0.0.1:5000")
}
