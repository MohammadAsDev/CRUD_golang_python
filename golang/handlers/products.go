package handlers

import (
	"net/http"

	"github.com/MohammadAsDev/CRUD_golang_python/conn"
	"github.com/MohammadAsDev/CRUD_golang_python/types"
	"github.com/gin-gonic/gin"
)

type ProductHandler struct {
	Db conn.Conn
}

func (handler *ProductHandler) CreateProduct(ctx *gin.Context) {
	request_body := types.AddProductRequest{}
	if err := ctx.BindJSON(&request_body); err != nil {
		ctx.AbortWithError(http.StatusBadRequest, err)
		return
	}

	product := &types.Product{
		ProductName:        request_body.ProductName,
		ProductDescription: request_body.ProductDescription,
	}

	db := handler.Db.GetDb()
	if result := db.Create(product); result.Error != nil {
		ctx.AbortWithError(http.StatusNotFound, result.Error)
		return
	}

	ctx.JSON(http.StatusCreated, product)
}

func (handler *ProductHandler) UpdateProduct(ctx *gin.Context) {
	id := ctx.Param("id")
	product_request := &types.AddProductRequest{}

	if err := ctx.BindJSON(product_request); err != nil {
		ctx.AbortWithError(http.StatusBadRequest, err)
		return
	}

	selected_product := &types.Product{}

	if result := handler.Db.GetDb().First(&selected_product, id); result.Error != nil {
		ctx.AbortWithError(http.StatusNotFound, result.Error)
		return
	}

	selected_product.ProductName = product_request.ProductName
	selected_product.ProductDescription = product_request.ProductDescription

	handler.Db.GetDb().Save(selected_product)
	ctx.JSON(http.StatusOK, selected_product)
}

func (handler *ProductHandler) DeleteProduct(ctx *gin.Context) {
	id := ctx.Param("id")
	deleted_product := &types.Product{}
	if result := handler.Db.GetDb().First(deleted_product, id); result.Error != nil {
		ctx.AbortWithError(http.StatusNotFound, result.Error)
		return
	}
	handler.Db.GetDb().Delete(deleted_product)
	ctx.Status(http.StatusOK)

}

func (handler *ProductHandler) GetProduct(ctx *gin.Context) {
	id := ctx.Param("id")
	product := &types.Product{}
	if result := handler.Db.GetDb().First(product, id); result.Error != nil {
		ctx.AbortWithError(http.StatusNotFound, result.Error)
		return
	}

	ctx.JSON(http.StatusAccepted, product)
}

func (handler *ProductHandler) ListProducts(ctx *gin.Context) {
	var products []types.Product
	if result := handler.Db.GetDb().Find(&products); result.Error != nil {
		ctx.AbortWithError(http.StatusNotFound, result.Error)
		return
	}
	ctx.JSON(http.StatusAccepted, &products)
}
