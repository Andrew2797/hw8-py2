from app import main
from flask import Flask, request, render_template, redirect
from app.routes.pizza import pizza_route
from app.models.pizza import Pizza
from app.models.ingredient import Ingredient
from app.models.base import create_db, Session



@pizza_route.route("/edit_pizza/<int:id>", methods=["GET", "POST"])
def edit_pizza(id):
    with Session() as session:
        pizza = session.query(Pizza).get(id)
        if request.method == "POST":
            pizza.name = request.form.get("name")
            pizza.price = float(request.form.get("price"))
            ingredients = request.form.getlist("ingredients")
            pizza.ingredients = session.query(Ingredient).filter(Ingredient.id.in_(ingredients)).all()
            session.commit()
            return redirect("/menu/")
        ingredients = session.query(Ingredient).all()
        return render_template("edit_pizza.html", pizza=pizza, ingredients=ingredients)

@pizza_route.route("/delete_pizza/<int:id>", methods=["POST"])
def delete_pizza(id):
    with Session() as session:
        pizza = session.query(Pizza).get(id)
        session.delete(pizza)
        session.commit()
    return redirect("/menu/")


if __name__ == "__main__":
    main()