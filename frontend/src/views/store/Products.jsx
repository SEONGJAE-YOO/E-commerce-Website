import React, {useState, useEffect} from 'react'
import apiInstance from '../../utils/axios'

function Products() {
    const [products, setProducts] = React.useState([])

    useEffect(() => {
        apiInstance.get('product/').then((response) => {
            setProducts(response.data)
        }).catch((error) => {
            console.error('Error fetching products: ', error)
        })
    }, [])

    return (
        <>
            <main className="mt-5">
                <div className="container">
                    <div className="row">
                        <div className="col-md-12">
                            <h2>Products</h2>
                            <div className="row">
                                {products.map((product) => (
                                    <div className="col-md-4" key={product.id}>
                                        <div className="card mb-4">
                                            <img src={product.image} style={{width:"100%", height:"200%"}} className="card-img-top" alt={product.name} />
                                            <div className="card-body">
                                                <h5 className="card-title">{product.name}</h5>
                                                <p className="card-text">{product.description}</p>
                                                <p className="card-text">Price: ${product.price}</p>
                                                <a href="#" className="btn btn-primary">Add to Cart</a>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </main>
    </>

    )
}

export default Products