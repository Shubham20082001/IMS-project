{
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Adding new Products",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j9rSMgKytN9V"
      },
      "source": [
        "## Read Data from JSON"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wlQdKmzYpRok"
      },
      "source": [
        "fd = open(\"record.json\",'r')\n",
        "r = fd.read()\n",
        "fd.close()\n",
        "\n",
        "record = json.loads(r)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N8fCrfQHqlUN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "04f7a640-bbad-429c-d7d1-686ca5ec14e2"
      },
      "source": [
        "record"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'1001': {'name': 'gold, 'pr': 100, 'qn': 34},\n",
              " '1002': {'name': 'silver', 'pr': 800, 'qn': 100},\n",
              " '1003': {'name': 'bronze', 'pr': 85, 'qn': 100},\n",
              " '1004': {'name': 'platinum', 'pr': 5, 'qn': 1000},\n",
              " '1005': {'name': 'Pen', 'pr': 20, 'qn': 100},\n",
              " '1006': {'name': 'Phone', 'pr': 50000, 'qn': 10},\n",
              " '1007': {'name': 'Mic', 'pr': 1500, 'qn': 0},\n",
              " '1008': {'name': 'diamond', 'pr': 599, 'qn': 5}}"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fNniKChHtFsH"
      },
      "source": [
        "## Add New Item into Inventory"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f61BridoqxZN",
        "outputId": "4919a5d7-b839-41df-ec08-b4f39107e984"
      },
      "source": [
        "prod_id = str(input(\"Enter product id:\"))\n",
        "name = str(input(\"Enter name:\"))\n",
        "pr = int(input(\"Enter price:\"))\n",
        "qn = int(input(\"Enter quantity:\"))\n",
        "\n",
        "record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}\n",
        "\n",
        "js = json.dumps(record)\n",
        "\n",
        "fd = open(\"record.json\",'w')\n",
        "fd.write(js)\n",
        "fd.close()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter product id:1009\n",
            "Enter name:Keyboard\n",
            "Enter price:1999\n",
            "Enter quantity:10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fqLcVGqqt_cO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "889a130b-8562-4a35-d430-645ff64724d3"
      },
      "source": [
        "record"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'1001': {'name': 'gold', 'pr': 100, 'qn': 34},\n",
              " '1002': {'name': 'silver', 'pr': 800, 'qn': 100},\n",
              " '1003': {'name': 'bronze', 'pr': 85, 'qn': 100},\n",
              " '1004': {'name': 'platinum', 'pr': 5, 'qn': 1000},\n",
              " '1005': {'name': 'Pen', 'pr': 20, 'qn': 100},\n",
              " '1006': {'name': 'Phone', 'pr': 50000, 'qn': 10},\n",
              " '1007': {'name': 'Mic', 'pr': 1500, 'qn': 0},\n",
              " '1008': {'name': 'Case', 'pr': 599, 'qn': 5},\n",
              " '1009': {'name': 'diamond', 'pr': 1999, 'qn': 10}}"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Mh8xAFUk7qFv"
      },
      "source": [
        "del record['1001']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n0UdHaVVFFLB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "af2d581b-583d-4be6-fd62-425bcd2343ea"
      },
      "source": [
        "record"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'1002': {'name': 'gold', 'pr': 800, 'qn': 100},\n",
              " '1003': {'name': 'silver', 'pr': 85, 'qn': 100},\n",
              " '1004': {'name': 'bronze', 'pr': 5, 'qn': 1000},\n",
              " '1005': {'name': 'platinum', 'pr': 20, 'qn': 100},\n",
              " '1006': {'name': 'Phone', 'pr': 50000, 'qn': 10},\n",
              " '1007': {'name': 'Mic', 'pr': 1500, 'qn': 0},\n",
              " '1008': {'name': 'Case', 'pr': 599, 'qn': 5},\n",
              " '1009': {'name': 'diamond', 'pr': 1999, 'qn': 10}}"
            ]
          },
          "metadata": {},
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zUa1OcFMFFmq"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}