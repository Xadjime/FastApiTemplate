
# cars path and query param
# id_counter = 1
# cars = []
# @app.get("/add_car")
# def read_item( name: str, price: int ):
#     global id_counter
#
#     for car in cars:
#        if car["name"].lower() == name.lower():
#            return {"error": f"Car {name} already exists"}
#
#     new_car = {
#         'id': id_counter,
#         'name': name,
#         'price': price
#     }
#     cars.append(new_car)
#     id_counter += 1
#
#     return {"message": f"Added {name} to cars"}
#
#
# @app.get("/cars")
# def read_cars():
#     return cars
#
#
# @app.get("/cars/{car_id}")
# def read_car(car_id: int):
#     for car in cars:
#         if car["id"] == car_id:
#             return car
#
#     return {"error": "car not found"}
#
# @app.get("/car_update/{car_id}")
# def update_car(car_id: int, name: str = None, price: int = None):
#     for car in cars:
#         if car["id"] == car_id:
#             if name is not None:
#                 car["name"] == name
#             if price is not None:
#                 car["price"] = price
#             return {"message": f" Succesfully updated car", "car": car}
#
#     return {"error": "car not found"}
#
#
# @app.get("/car_del/{car_id}")
# def delete_car(car_id: int):
#     for car in cars:
#         if car["id"] == car_id:
#             cars.remove(car)
#             return {"message": f" Succesfully deleted car", "car": car}
#
#     return {"error": "car not found"}


#
# @app.get("/car_list", tags=["Templates"])
# async def car_list(request: Request):
#     return templates.TemplateResponse(request, name="car_list.html", context={"cars": cars})
#
#
# @app.get("/add_car", tags=["Templates"])
# async def car_create_page(request: Request):
#     return templates.TemplateResponse(request, name="car_create.html")
#
#
# @app.post("/add_car")
# async def car_create(name: str = Form(...), price: int = Form(...)):
#     global id_counter
#     cars.append({
#         'id': id_counter,
#         'name': name,
#         'price': price
#     })
#     id_counter += 1
#     # Redirect to list view so browser doesn't re-submit form on refresh
#     return RedirectResponse(url="/car_list", status_code=status.HTTP_303_SEE_OTHER)
#
#
# @app.get("/update_car/{car_id}", tags=["Templates"])
# async def car_update_page(request: Request, car_id: int):
#     # Find car to pre-fill the edit form
#     car = next((c for c in cars if c["id"] == car_id), None)
#     if not car:
#         return RedirectResponse(url="/car_list", status_code=status.HTTP_303_SEE_OTHER)
#     return templates.TemplateResponse(request, name="car_update.html", context={"car": car})
#
#
# @app.post("/update_car/{car_id}")
# async def car_update(car_id: int, name: str = Form(...), price: int = Form(...)):
#     for car in cars:
#         if car["id"] == car_id:
#             car["name"] = name
#             car["price"] = price
#             break
#
#     return RedirectResponse(url="/car_list", status_code=status.HTTP_303_SEE_OTHER)
#
#
# @app.post("/delete_car/{car_id}")
# async def car_delete(car_id: int):
#     for car in cars:
#         if car["id"] == car_id:
#             cars.remove(car)
#             break
#
#     return RedirectResponse(url="/car_list", status_code=status.HTTP_303_SEE_OTHER)


# Todo template query
# todos = []
# @app.get("/todo_list", tags=["Templates"])
# async def todo_list(request: Request):
#     return templates.TemplateResponse(request, name="todo_list.html", context={"todos": todos})
#
# @app.get("/todo_create", tags=["Templates"])
# async def todo_create_page(request: Request):
#     return templates.TemplateResponse(request, name="todo_create.html")
#
#
# @app.post("/todo_create", tags=["Templates"])
# async def todo_create(
#         title: str = Form(...),
#         description: Optional[str] = Form(None),
#         stat: Optional[str] = Form(None),
#         create_date: datetime = Form(...)
# ):
#     global id_counter
#
#
#     is_completed = True if stat == "on" else False
#
#     new_todo = {
#         'id': id_counter,
#         'title': title,
#         'description': description,
#         'create_date': create_date,
#         'stat': is_completed,
#     }
#     todos.append(new_todo)
#     id_counter += 1
#
#     return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)
#
#
# @app.get("/todo_update/{todo_id}", tags=["Templates"])
# async def todo_update_page(request: Request, todo_id: int):
#     todo = next((t for t in todos if t["id"] == todo_id), None)
#     if not todo:
#         return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)
#
#     return templates.TemplateResponse(request, name="todo_update.html", context={"todo": todo})
#
#
# @app.post("/todo_update/{todo_id}", tags=["Templates"])
# async def todo_update(
#     todo_id: int,
#     title: str = Form(...),
#     description: Optional[str] = Form(None),
#     stat: Optional[str] = Form(None),
#     create_date: datetime = Form(...)
# ):
#     for todo in todos:
#         if todo["id"] == todo_id:
#             todo["title"] = title
#             todo["description"] = description
#             todo["stat"] = True if stat == "on" else False
#             todo["create_date"] = create_date
#             break
#
#     return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)
#
#
# @app.post("/todo_delete/{todo_id}", tags=["Templates"])
# async def car_delete(todo_id: int):
#     for todo in todos:
#         if todo["id"] == todo_id:
#             todos.remove(todo)
#             break
#
#     return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)



# # Product
# # ---------- CREATE ----------
# @app.post("/product/create", status_code=status.HTTP_201_CREATED , tags=["product"])
# async def product_create(product_form: ProductCreate, session: SessionDep):
#     instance = Product(**product_form.model_dump())
#     session.add(instance)
#     session.commit()
#     session.refresh(instance)  # id ni olish uchun
#     return {"message": "Success create!", "status": 201, "data": instance}
#
#
# # ---------- READ ----------
# @app.get("/product/list", tags=["product"])
# async def product_list(session: SessionDep):
#     products = session.exec(select(Product)).all()
#     return products
#
#
# # ---------- DETAIL ----------
# @app.get("/product/{product_id}", tags=["product"])
# async def product_detail(product_id: int, session: SessionDep):
#     product = session.get(Product, product_id)
#     if not product:
#         raise HTTPException(status_code=404, detail="Product nof found!")
#     return product
#
#
# # ---------- UPDATE ----------
# @app.patch("/product/{product_id}/update", tags=["product"])
# async def product_partial_update(product_id: int, product_form: ProductUpdate, session: SessionDep):
#     product = session.get(Product, product_id)
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found!")
#     data = product_form.model_dump(exclude_unset=True)
#     for key, value in data.items():
#         setattr(product, key, value)
#     session.add(product)
#     session.commit()
#     session.refresh(product)
#     return {"message": "Success partial update!", "status": 200, "data": product}
#
#
# # ---------- DELETE ----------
# @app.delete("/product/{product_id}/delete", tags=["product"])
# async def product_delete(product_id: int, session: SessionDep):
#     product = session.get(Product, product_id)
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found!")
#     session.delete(product)
#     session.commit()
#     return {"message": "Success delete!", "status": 200}
#
#
# # Category
# # ---------- CREATE ----------
# @app.post("/category/create", status_code=status.HTTP_201_CREATED, tags=["category"])
# async def category_create(category_form: CategoryCreate, session: SessionDep):
#     instance = Category(**category_form.model_dump())
#     session.add(instance)
#     session.commit()
#     session.refresh(instance)  # id ni olish uchun
#     return {"message": "Success create!", "status": 201, "data": instance}
#
#
# # ---------- READ ----------
# @app.get("/category/list", tags=["category"])
# async def category_list(session: SessionDep):
#     categories = session.exec(select(Category)).all()
#     return categories
#
#
# # ---------- DETAIL ----------
# @app.get("/category/{category_id}", tags=["category"])
# async def category_detail(category_id: int, session: SessionDep):
#     category = session.get(Category, category_id)
#     if not category:
#         raise HTTPException(status_code=404, detail="Category nof found!")
#     return category
#
#
# # ---------- UPDATE ----------
# @app.patch("/category/{category_id}/update", tags=["category"])
# async def category_partial_update(category_id: int, category_form: CategoryUpdate, session: SessionDep):
#     category = session.get(Category, category_id)
#     if not category:
#         raise HTTPException(status_code=404, detail="Category not found!")
#     data = category_form.model_dump(exclude_unset=True)
#     for key, value in data.items():
#         setattr(category, key, value)
#     session.add(category)
#     session.commit()
#     session.refresh(category)
#     return {"message": "Success partial update!", "status": 200, "data": category}
#
#
# # ---------- DELETE ----------
# @app.delete("/category/{category_id}/delete", tags=["category"])
# async def category_delete(category_id: int, session: SessionDep):
#     category = session.get(Category, category_id)
#     if not category:
#         raise HTTPException(status_code=404, detail="Category not found!")
#     session.delete(category)
#     session.commit()
#     return {"message": "Success delete!", "status": 200}


# class ProductCreate(BaseModel):
#     title: str
#     photo: Optional[str] = None
#     category_id: int
#     price: int
#
# class ProductUpdate(BaseModel):
#     title: Optional[str] = None
#     photo: Optional[str] = None
#     category_id: Optional[int] = None
#     price: Optional[int] = None
#
# class CategoryCreate(BaseModel):
#     title: str
#
# class CategoryUpdate(BaseModel):
#     title: Optional[str] = None



# todos = []

# id_counter = 1




# #  TODO
# @app.get("/todo_list", tags=["Templates"])
# async def todo_list(request: Request):
#     return templates.TemplateResponse(request, name="todo_list.html", context={"todos": todos})
#
# @app.get("/todo_create", tags=["Templates"])
# async def todo_create_page(request: Request):
#     return templates.TemplateResponse(request, name="todo_create.html")
#
#
# @app.post("/todo_create", tags=["Templates"])
# async def todo_create(
#         title: str = Form(...),
#         description: Optional[str] = Form(None),
#         stat: Optional[str] = Form(None),
#         create_date: datetime = Form(...)
# ):
#     global id_counter
#
#
#     is_completed = True if stat == "on" else False
#
#     new_todo = {
#         'id': id_counter,
#         'title': title,
#         'description': description,
#         'create_date': create_date,
#         'stat': is_completed,
#     }
#     todos.append(new_todo)
#     id_counter += 1
#
#     return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)
#
#
# @app.get("/todo_update/{todo_id}", tags=["Templates"])
# async def todo_update_page(request: Request, todo_id: int):
#     todo = next((t for t in todos if t["id"] == todo_id), None)
#     if not todo:
#         return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)
#
#     return templates.TemplateResponse(request, name="todo_update.html", context={"todo": todo})
#
#
# @app.post("/todo_update/{todo_id}", tags=["Templates"])
# async def todo_update(
#     todo_id: int,
#     title: str = Form(...),
#     description: Optional[str] = Form(None),
#     stat: Optional[str] = Form(None),
#     create_date: datetime = Form(...)
# ):
#     for todo in todos:
#         if todo["id"] == todo_id:
#             todo["title"] = title
#             todo["description"] = description
#             todo["stat"] = True if stat == "on" else False
#             todo["create_date"] = create_date
#             break
#
#     return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)
#
#
# @app.post("/todo_delete/{todo_id}", tags=["Templates"])
# async def car_delete(todo_id: int):
#     for todo in todos:
#         if todo["id"] == todo_id:
#             todos.remove(todo)
#             break
#
#     return RedirectResponse(url="/todo_list", status_code=status.HTTP_303_SEE_OTHER)
