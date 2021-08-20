using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class check : MonoBehaviour
{
    [SerializeField] Text Error;
    
    // Start is called before the first frame update
    void Start()
    {
        Error.gameObject.SetActive(false);
        StartCoroutine(checkInternetConnection((isConnected) =>
        {

            if (isConnected)
            {
                print("connected");
                
            }
            else
            {
                print("Not connected");
                Error.gameObject.SetActive(true);
                //Application.Quit();

            }
        }
            ));
    }

    // Update is called once per frame
    void Update()
    {

    }

    IEnumerator checkInternetConnection(Action<bool> action)
    {
        WWW www = new WWW("http://google.com");
        yield return www;
        if (www.error != null)
        {
            action(false);
        }
        else
        {
            action(true);
        }

    }
}
