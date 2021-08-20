using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

[System.Serializable]
public class ProductDetails
{
    public int id;
    public string name;
    public float price;
    public float rating;
    public string description;
}

[System.Serializable]
public class ProductRoot
{
    public int count;
    public List<ProductDetails> results;
}

public class script_add : MonoBehaviour
{
    string jsonURL = "http://143.110.189.18/products/";
    public TextMesh t;



    void Start()
    {
        StartCoroutine(GetProductData(jsonURL));
    }

    IEnumerator GetProductData(string url2)
    {


        UnityWebRequest request = UnityWebRequest.Get(url2);
        yield return request.SendWebRequest();

        if (request.isNetworkError)
        {
            //error...
        }
        else
        {


            Debug.Log("Hello World");

            //GameObject.Find("NEW TEXT").GetComponent<TextMesh>();
            //success...
            int size = 16;
            GameObject[] pd;
            //public GameObject sel;

            byte[] result = request.downloadHandler.data;
            string shopJSON = System.Text.Encoding.Default.GetString(result);
            string name = "";

            ProductRoot rootProduct = JsonUtility.FromJson<ProductRoot>(request.downloadHandler.text);
            string[] abc = new string[] { "The Silva mind control method", "Arthur Hailey WHEELS", "Seagate harddrive", "Boya BYM1 Condenser Microphone", "Toy phone", "Ganesh Idol", "Magnetic Train", "Pen holder", "Nescafe Coffee", "Wagh Bakri Premium Tea", "Maggi Noodles", "Word power made easy", "Toy Helicopter", "Boat Basshead earphones", "Teddy doll", "BluestarAc", "Table clock"};

            for (int i = 0; i < size; i++)
            {
                GameObject go = transform.GetChild(i).gameObject;
                string temp = abc[i];
                //Debug.Log(temp);
                bool product_found = false;

                for (int j = 0; j < rootProduct.count; j++)
                {

                    name = rootProduct.results[j].name;

                    if (name == temp)
                    {
                        string deatials = rootProduct.results[j].description;
                        float price = rootProduct.results[j].price;
                        float rating = rootProduct.results[j].rating;
                        go.transform.GetChild(0).GetComponent<TextMesh>().text = name + "\n " + deatials + " \n Price: $" + price + " \n Rating: " + rating;
                        Debug.Log(name + " --Product found");
                        product_found = true;
                    }


                }
                if (product_found == false)
                {
                    go.transform.GetChild(0).GetComponent<TextMesh>().text = temp + "\n Will update the data soon";
                }


            }

        }
    }
}

